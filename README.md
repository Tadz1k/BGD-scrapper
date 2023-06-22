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
    sudo mkdir /mnt/bgd-olx-fileshare
    ```
    <br />

    2. Install Azure Utils
    ```bash
    sudo apt-get install cifs-utils
    ```

    <br />

    3. Mount disk created in Azure

        This command should be taken from Azure -> Storage Account -> File Share -> Connect -> Linux

    4. Run mongo
    ```bash
    sudo docker pull mongo
    sudo docker run -d -v /mnt/bgd-olx-fileshare:/data/db --name mongodb -p 27017:27017 mongo
    ```
    <br />

* otherwise start container
    ```bash
    sudo docker start {containerid} 
    ```

### Connect
```bash
sudo docker exec -it mongodb mongosh
```

## Run the application
1. Clone repository
```bash
git clone https://github.com/Tadz1k/BGD-scrapper
```

2. Set up Python environment
```bash
python3 -m venv venv
source venv/vin/activate
pip install -r BGD-scrapper/requirements.txt
```

3. Run application
```bash
python3 ./BGD-scrapper 
```