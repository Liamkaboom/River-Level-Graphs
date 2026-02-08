# South Forty Foot Drain Boston (Black Sluice) - River Level Graphs

A python program to visualise daily maximum River Levels at the South Forty Foot drain in Boston. (Well, in theory any type of .csv data).

This simple project was created because I was bored, and the South Forty Foot Drain in Boston having flooded back in January 2025 - this could prove to be quite useful.

Following some research, pandas appeared to be the best library to work with matplotlib for this, rather than numpy - so that's what I went with. There are 2 python files - one for analysing the maximum river levels when it flooded last January, and one to analyse the maximum river levels between 2 user inputted dates - the data in the csv file goes back to late 2020.

Please bare in mind that this monitoring station can only go up to 2.3m (Hence 3 days of that max level in January 2025). The estimated river level at the time of flooding was 3.192m (see PDF in repo for EA analysis of the flooding) - Nearly 1m higher than the station in Boston can reach.

UPDATE 2: Added RecentLevels.py - Found out how to access the latest levels from the stationm, in JSON format. This program allows you to select 2 recent dates and see the river levels inbetween.

This is verion 2 of this mini project - more will be coming at later dates.

**© @BostonWeatherUK 2026**
This project completely free to use and modify, but with credit to *@BostonWeatherUK*.