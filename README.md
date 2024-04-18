<h1 align="center">
<a  href=""><img src="https://github.com/dkb4rb/ProxFuzzer/blob/main/assets/image.svg" alt="ProxFuzzer" width="300" style="margin-left: 250px!importan;"></a>
<br>
ProxFuzzer
</h1>

<h4 align="center">A minimal Tool to fuzzing and bypass Proxy parameter and security <a href="http://electron.atom.io" target="_blank">Electron</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">Como usar</a> •
  <a href="#download">Download</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://github.com/dkb4rb/ProxFuzzer/blob/main/assets/Present.gif))

# Key Features

- **Importación de Módulos:**
  - El script importa los módulos necesarios, como `sys`, `requests`, `termcolor`, y `pwn`.

- **Impresión de Banner en Colores:**
  - Utiliza códigos ANSI para imprimir un banner en colores llamativos en la consola.

- **Función de Fuzzing de URL:**
  - Define una función `fuzz_url(url_ready)` que realiza una solicitud HTTP GET a una URL y verifica si el código de estado es 200. En caso afirmativo, imprime un mensaje de éxito.

- **Ejecución del Fuzzing:**
  - La función `run_fuzz(url, wordlist)` toma una URL base y una ruta de archivo de wordlist, abre el archivo de wordlist y llama a `fuzz_url` para cada línea del archivo.

- **Manejo de Argumentos de Línea de Comandos:**
  - Verifica que se proporcionen exactamente dos argumentos de línea de comandos (URL base y ruta del wordlist). En caso contrario, muestra un mensaje de uso y sale del script.

- **Interfaz de Usuario Mejorada:**
  - Imprime un banner colorido y usa la librería `pwn` para resaltar información importante, como la URL base y la ruta del wordlist.

- **Uso de Colores y Estilos de Texto:**
  - Utiliza la librería `termcolor` para imprimir texto en colores y estilos específicos, mejorando la legibilidad y la presentación del output.

- **Compatibilidad con la Ejecución Directa y como Módulo:**
  - Utiliza `if __name__ == "__main__":` para permitir la ejecución del script directamente desde la línea de comandos, así como la importación segura como módulo en otros scripts.

# Cómo Usar

1. **Requisitos Previos:**
   - Asegúrate de tener instalado Python en tu sistema.
   - Instala las dependencias necesarias ejecutando `pip install requests termcolor pwntools`.

2. **Descarga el Script:**
   - Descarga el script Python y guárdalo en tu sistema con el nombre `script.py`.

3. **Ejecución desde la Línea de Comandos:**
   - Abre una terminal o línea de comandos en tu sistema.

4. **Ejecutar el Script:**
   - Ejecuta el script Python proporcionando dos argumentos:
     ```
     python script.py <URL base> <ruta del wordlist>
     ```
     - `<URL base>`: La URL base que deseas probar.
     - `<ruta del wordlist>`: La ruta del archivo de wordlist que contiene las rutas adicionales a probar.

5. **Interpretación de Resultados:**
   - El script comenzará a probar cada ruta del wordlist en la URL base proporcionada.
   - Los resultados se imprimirán en la consola, indicando si se encontraron recursos válidos (código de estado 200) o no.

6. **Análisis de Resultados:**
   - Analiza los resultados impresos en la consola para identificar recursos válidos y posibles vulnerabilidades en la aplicación web.

7. **Personalización Adicional:**
   - Puedes modificar el banner, ajustar los colores o expandir la funcionalidad del script según tus necesidades específicas.

8. **¡Experimenta!**
   - ¡Experimenta con diferentes wordlists y URL base para encontrar posibles puntos de entrada en la aplicación web objetivo!


```bash
# Clone this repository
$ git clone https://github.com/dkb4rb/ProxFuzzer.git

# Go into the repository
$ cd ProxFuzzer

# Run the app
$ python3 fuzzer_proxy_rotes.py <URL> <WORDLIST>
```

## Support

<a href="https://www.buymeacoffee.com/" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License

MIT

---

> [amitmerchant.com](https://dkb4rb.github.io) &nbsp;&middot;&nbsp;
> GitHub [@Dkb4rb](https://github.com/dkb4rb) &nbsp;&middot;&nbsp;

