# plant_tracker

Communication Contract

The following text files must be created in your local direcotry before use: run.txt, water.txt, fertilizer.txt, date.txt, schedule.txt.
The schedule.txt file must contain each plants watering and fertilzing schedule, including the intervals(#days) between each watering and refertilizing. The structure for which the data needs to be provided is in a string 'PlantName' water_interval fertilizer_interval 'date_watered' 'date_fertilized'
The water_interval and fertilize_interval represent the amount of days between watering and or fertilizing. The 'date_watered' and 'date_fertilized' need to be provided in string format 'YEAR-MM-DD'. Lastly, each plant's data needs to be stored on a new line in the schedule.txt file. 

The following packages must be installed: time, dateime

A. How to request data: In order to request data plant_tracker.py should be running. Tha main application will send a request every 24 hours by writing 'run' to run.txt. Plant_tracker.py will be listening and when it reads 'run', it will read the lines of the schedule.txt file and convert the data to a list of plants. Plant_tracker will then iterate through each plant and determine which plants need to be watered or fertilized that day. The current date, found from the imported datetime module, will be used to subtract the dates in which the plant was last watered or fertilized and compare those values to the water_interval and fertilize_interval to determine if the plant needs to be watered and/or fertilized. 


B. How to receive data: Plant_tracker will write the plants to the water.txt file or fertilizer.txt file if the amount of days since the plants have been watered or fertilized is >= their designated intervals(>= in the event a day is missed). The response will be written as a string, and if multiple plants are written to a file each plant will be on a new line. In addition, since datetime was used to determine the current date, plant_tracker will also write the date to the date.txt file. Once plant_tracker has written to files the 'run' in run.txt file should be erased. To receive the response, the main application will sleep for 2 seconds to give plant_tracker time to write to each of the txt files. It should then read all the lines in water.txt, fertilizer.txt, and date.txt. If a plant is scheduled to be watered or fertilized the schedule.txt file will need to be updated with current date. After reading these files, the data should be removed from water.txt, fertilizer.txt, and date.txt to avoid errors when plant_tracker receives a new request. 


Example Call to request and receive, 

![image](https://user-images.githubusercontent.com/81596877/181143111-025cde45-391c-456b-afcf-30a1fb2a7f84.png)![image](https://user-images.githubusercontent.com/81596877/181142902-f9779292-a781-410e-bf81-5d8504b2b344.png)

UML:
![image](https://user-images.githubusercontent.com/81596877/181142966-67dba3bf-e11e-4fc0-9083-cb6dae7d081c.png)
