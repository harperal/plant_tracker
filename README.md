# plant_tracker

Communication Contract

The following text files must be created in your local direcotry before use: run.txt, water.txt, fertilizer.txt, date.txt, schedule.txt.
The schedule.txt file must contain each plants watering and fertilzing schedule, including the intervals(#days) between each watering and refertilizing. The structure for which the data needs to be provided is in a string 'PlantName' water_interval fertilizer_interval 'date_watered' 'date_fertilized'
The water_interval and plant interval represent the amount of days between watering and or fertilizing. The 'date_watered' and 'date_fertilized' need to be provided in string format 'YEAR-MM-DD'. Lastly, each plant's data needs to be stored on a new line in the schedule.txt file. 

The following packages must be installed: time, dateime

A. How to request data: calorie_service.py should be started, and will give the message 'listening' to the terminal. When a user inputs a food keyword in the calorie search function from the main application, the main app should write 'run' to init_search.txt, and then write the keyword to keyword.txt . As calorie_service.py listens, when it reads 'run', it will then read the user input from keyword.txt. calorie_service will then scrape google search with the user input, and get calories for food from user_input

B. How to receive data: Calorie_service will write the found calories to line one of calories.txt, then write the corresponding serving size and unit of measurement to line two. The response will be written as a string. To receive the response, the main application should first sleep for 6 to 10 seconds to give the calorie_service time to scrape, depending on internet connection speed for the device running the program. It then should read lines 1 and 2 from calories.txt. If calorie_service finds no information for user input from keyword.txt, then it will write 'None' to calories.txt. Finally the main application should erase calories.txt after reading it to prevent errors.

Example Call to request and receive, 

![image](https://user-images.githubusercontent.com/81596877/181143111-025cde45-391c-456b-afcf-30a1fb2a7f84.png)![image](https://user-images.githubusercontent.com/81596877/181142902-f9779292-a781-410e-bf81-5d8504b2b344.png)

UML:
![image](https://user-images.githubusercontent.com/81596877/181142966-67dba3bf-e11e-4fc0-9083-cb6dae7d081c.png)
