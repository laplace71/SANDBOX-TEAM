using System;

namespace BasicLogin
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Sistema de Login Básico ===");
            
            Console.Write("Usuario: ");
            string username = Console.ReadLine();
            
            Console.Write("Contraseña: ");
            
            // Ocultar contraseña en consola (opcional para mostrar, pero un detalle bonito)
            string password = "";
            ConsoleKeyInfo key;
            
            do
            {
                key = Console.ReadKey(true);
                if (key.Key != ConsoleKey.Backspace && key.Key != ConsoleKey.Enter)
                {
                    password += key.KeyChar;
                    Console.Write("*");
                }
                else if (key.Key == ConsoleKey.Backspace && password.Length > 0)
                {
                    password = password.Substring(0, (password.Length - 1));
                    Console.Write("\b \b");
                }
            }
            while (key.Key != ConsoleKey.Enter);

            Console.WriteLine();

            // Validación básica (solo de muestra)
            if (username == "admin" && password == "12345")
            {
                Console.WriteLine("\n[+] ¡Login exitoso! Bienvenido, " + username + ".");
            }
            else
            {
                Console.WriteLine("\n[-] Error: Usuario o contraseña incorrectos.");
            }
            
            Console.WriteLine("\nPresiona cualquier tecla para salir...");
            Console.ReadKey();
        }
    }
}
