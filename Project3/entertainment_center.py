#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:55:26 2017

@author: asenden
"""

import media
import fresh_tomatoes

gone_in_60_seconds = media.Movie("Gone in 60 Seconds",
                                 '''He has no choice to return to his life of crime when his kid brother gets in some 
                                 life-threatening trouble''',
                                 "https://i.ytimg.com/vi/kGvuZ4r2bhs/maxresdefault.jpg",
                                 "https://www.youtube.com/watch?v=o6AyAM1buQ8",
                                 "https://www.rottentomatoes.com/m/1097865-gone_in_60_seconds/reviews/")

hidden_figures = media.Movie("Hidden Figures", 
                             '''The untold story of how 3 females served as the brains behind the launch of an astronaut 
                             into space, restoring the nation's confidence in the Space Race.''',
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_"
                             "Figures%2C_2016.jpg",
                             "https://www.youtube.com/watch?v=RK8xHq6dfAo",
                             "https://www.rottentomatoes.com/m/hidden_figures/reviews/")

big_hero_6 = media.Movie("Big hero 6",
                         '''His older brother, a robotics major, built a first-aid robot to assist with diagnosing people. 
                         After his death, Hiro and his friends get into the middle of a dangerous plot and transform the 
                         robot into one that can fight battles.''',
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1"
                         "YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY1200_CR105,0,630,1200_AL_.jpg",
                         "https://www.youtube.com/watch?v=rD5OA6sQ97M",
                         "https://www.rottentomatoes.com/m/big_hero_6/reviews/")

freedom_writers = media.Movie("Freedom Writers",
                              '''A story of a dedicated teacher in a racially divided school teaching students seemingly 
                              incapable of learning. Her vow to not give up inspires her students to take an interest in 
                              their own education''',
                              "https://resizing.flixster.com/r_MZ83bRofGXj1ldC44Tg33d30I=/206x305/v1.bTsxMTIxNjMzMDtqOz"
                              "E3NTg5OzEyMDA7MTUzNjsyMDQ4",
                              "https://www.youtube.com/watch?v=JhXMJlm852A",
                              "https://www.rottentomatoes.com/m/freedom_writers/reviews/")

the_guardian = media.Movie("The Guardian",
                           '''A Coast Guard rescue swimmer mourns the loss of his crew in a fatal accident and copes by 
                           dedicating himself to training new recruits. He comes to mold a cocky young swim champ into 
                           his protege and takes him on a mission in the dangerous waters of the Bering Strait''',
                           "https://resizing.flixster.com/DOZrQ5_kmA_dmCsY2OC7YL7Txuo=/206x305/v1.bTsxMTYxODg4OTtqOzE3NT"
                           "k0OzEyMDA7NzUwOzEwMDA",
                           "https://www.youtube.com/watch?v=tZy-wcQIsRU",
                           "https://www.rottentomatoes.com/m/the_guardian_2006/reviews/")

wonder_woman = media.Movie("Wonder Woman",
                           '''She was not always Wonder Woman. Growing up on a sheltered island, she met an American pilot 
                           who told her of the massive conflict that's raging in the outside world. She believed she could 
                           stop this threat and left the island to fight alongside men in war to end all wars.''',
                           "https://images-na.ssl-images-amazon.com/images/I/91I2JspDFLL._RI_.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                           "https://www.rottentomatoes.com/m/wonder_woman_2017/reviews/")

movies_list = [gone_in_60_seconds, hidden_figures, big_hero_6, freedom_writers, the_guardian, wonder_woman]
    #list of movies I've chosen and described to be on the webpage

fresh_tomatoes.open_movies_page(movies_list)
    #this command calls on the fresh_tomatoes file and opens a browser to display the movies listed in this file


