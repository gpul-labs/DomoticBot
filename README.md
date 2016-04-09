# Bot Telegram
--------------

# Comandos básicos
    - /start
    - /help
    - /stop

# Funcionalidades
    - Enviar temperatura deseada
        - /temp
        - {climate control device}
        - {target degrees temperature}
        - [ + | - ]{threshold room temperature}
            (default threshold room temperature more +-3)

        - Sample:
            /temp
            climate-control-cocina
            23
            -20

    - Notificaciones periodicas sobre la temperatura cierto tiempo
        - /temp notify on
        - {minutes period}
        - /temp notify off

    - Ver lista de opciones
        - /list

    - Ver lista de dispositivos
        - /device
        climate-control-cocina

    - Ver estados
        - /status

# Pasos
    1. [Telepot](https://github.com/nickoala/telepot). Python framework for Telegram Bot API.
        - [Supports inline mode](https://core.telegram.org/bots/inline)
        - See [samples](https://core.telegram.org/bots/samples)
    2. Crear bot y solicitar token
        - Install Bot [BotFather](https://telegram.me/botfather)
```telegram
            - /start
            - /newbot - create a new bot
            - /token - generate authorization token
```
    3. Conectar sensores a la RaspberryPi. 
        - Ver [charla2](https://github.com/gpul-labs/charla-2) de GPUL Labs by @ResonantWave
    4. Evitar DDoS poniendo sleep entre cada petición
        ```php
    if ($http_code >= 500) {
        // do not want to DDOS server if something goes wrong
        sleep(10);
        return false;
      }
        ```  
    5. Setup Bot
        - [Python samples](https://pythonhosted.org/twx/twx/botapi/botapi.html)

# License
---------
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

More info in "LICENSE" file
