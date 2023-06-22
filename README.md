# Big Data application - cars ads webscrapper

## Purpose
The purpose of the application is to gather car ads from multiple webpages for further analysis and visualizations

## Authors
- Adrian Kordas
- Filip Dzięcioł

## Installation
### Prerequisits
- (Optionally) Cloud Account (currently Azure)
- Machine to run the application (currently Azure VM)
- Git installed
- Docker installed

### Installation steps
* If running first time:

    1. Create data share
    ```bash
    sudo mkdir /mnt/bgdstorageolx
    ```
    <br />

    2. Install Azure Utils
    ```bash
    sudo apt-get install cifs-utils
    ```

    <br />

    3. Mount disk created in Azure
    ```bash
    sudo mount -t cifs //{accountname}.file.core.windows.net/{diskname} /mnt/bgdstorageolx -o vers=3.0,username={username},password={password},dir_mode=0777,file_mode=0777,serverino
    ```

    4. Run mongo
    ```bash
    sudo docker pull mongo
    sudo docker run -d -v /mnt/bgdstorageolx:/data/db --name mongodb -p 27017:27017 mongo
    ```
    <br />

* otherwise start container
    ```bash
    sudo docker start {containerid} 
    ```