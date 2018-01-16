#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:32:01 2017

@author: asenden
"""

import webbrowser

class Movie():
    '''This class provides a way to store movie related information.'''
    
    def __init__(self, movie_title, movie_storyline, movie_image, movie_trailer, movie_reviews):
        '''Function is called on an instance of Movie class for each movie listed in entertainment_center.py file
        and is a way for the movie class to store different pieces of information about the movie denoted.
        The arguments are assigned to corresponding instance variables:
            self.title = holds the title the movie for instance called
            self.storyline = holds storyline of movie for instance called
            self.poster_image_url = holds the cover image of the movies for the instance called
            self.trailer_youtube_url = holds the url of the movie trailer of the instance called
            self.reviews = holds a url to the reviews of the movie for the instance called
        Returns:
            Returns an instance of the movie called and it's corresponding instance variable.'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer
        self.reviews = movie_reviews
        
    def show_trailer(self):
        '''Function is called on an instance of Movie class for each movie denoted in the entertainment_center.py file
        and then a browser will open and start playing the trailer for again the movie denoted.
        The argument assigned to the corresponding instance variable:
            Opens a web broswer and starts to play that movie's trailer.'''
        webbrowser.open(self.trailer_youtube_url)