using System;
using System.IO;
using System.IO.Compression;
using System.Threading;
using StackExchange.Redis;
using MongoDB.Driver;
using MongoDB.Bson;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            // Procesar datos desde Redis
            ProcessDataFromRedis();

            // Esperar 1 segundo antes de verificar de nuevo
            Thread.Sleep(1000);
        }
    }

    static void ProcessDataFromRedis()
    {
        // Conexión a Redis
        ConnectionMultiplexer redis = ConnectionMultiplexer.Connect("localhost");
        IDatabase db = redis.GetDatabase();

        // Recuperar el valor de la clave 'uploaded_zip' de Redis
        RedisValue uploadedZip = db.StringGet("uploaded_zip");

        // Si no hay datos en Redis, salir del método
        if (uploadedZip.IsNullOrEmpty)
        {
            return;
        }

        // Descomprimir el archivo ZIP
        using (MemoryStream ms = new MemoryStream((byte[])uploadedZip))
        using (ZipArchive zipArchive = new ZipArchive(ms))
        {
            // Conexión a MongoDB
            MongoClient mongoClient = new MongoClient("mongodb://localhost:27017");
            IMongoDatabase database = mongoClient.GetDatabase("test");

            foreach (ZipArchiveEntry entry in zipArchive.Entries)
            {
                if (entry.FullName.EndsWith(".TXT"))
                {
                    // Obtener el nombre del archivo sin la extensión
                    string fileNameWithoutExtension = Path.GetFileNameWithoutExtension(entry.FullName);

                    // Determinar el tipo según el nombre del archivo
                    string type = fileNameWithoutExtension.EndsWith("Spectra") ? "spectra" : "waveform";

                    // Leer los datos del archivo
                    using (StreamReader reader = new StreamReader(entry.Open()))
                    {
                        string data = reader.ReadToEnd();

                        // Insertar los datos en la colección correspondiente en MongoDB
                        IMongoCollection<BsonDocument> collection = database.GetCollection<BsonDocument>(type);
                        BsonDocument doc = new BsonDocument
                        {
                            { "file_name", entry.FullName },
                            { "data", data }
                        };
                        collection.InsertOne(doc);
                    }
                }
            }
        }

        // Limpiar la clave 'uploaded_zip' en Redis
        db.KeyDelete("uploaded_zip");

        Console.WriteLine("Datos transferidos de Redis a MongoDB con éxito.");
    }
}
