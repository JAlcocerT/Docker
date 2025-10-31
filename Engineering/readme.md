
> For other engineering tools: https://jalcocert.github.io/Linux/docs/debian/foss_engineering/

Chili3d: This is an open-source, web-based 3D CAD application for online model design and editing.

```sh
sudo docker compose -f ./CAD/docker-compose.yml up -d
```

See also:

1. OctoPrint,"Most consumer printers (Marlin, etc.)","The gold standard with a massive plugin ecosystem (timelapses, AI failure detection, bed leveling visualization).","100% Open Source. Typically installed on a Raspberry Pi (via the OctoPi image) or a server, providing a full web interface to control the printer, upload G-code, and monitor prints with a webcam."

2. Mainsail,Klipper Firmware Required,"Sleek, modern, and highly responsive UI. Specifically designed to work with the high-performance Klipper firmware.","100% Open Source. Runs on a Raspberry Pi or any Linux machine, acting as the web front-end for the Klipper/Moonraker backend."

3. Fluidd,Klipper Firmware Required,"Very similar to Mainsail; also a clean, responsive web interface for Klipper. Features G-code editing, bed mesh leveling, and multiple webcam support.","100% Open Source. Like Mainsail, it is a web front-end for the Klipper/Moonraker stack, making it a powerful, self-hosted alternative to OctoPrint."