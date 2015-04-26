#!/usr/bin/env python

import media
import fresh_tomatoes as ft

def main():

    #store list of movies
    movies = [
        media.Movie(
            title = 'The Avengers: Age of Ultron',
            poster_image_url = 'http://www.movieposterdb.com/posters/15_03/2015/2395427/l_2395427_e80a54df.jpg',
            trailer_youtube_url = 'https://www.youtube.com/watch?v=JAUoeqvedMo',
            director = 'Joss Whedon',
            actors = ['Robert Downey Jr.', 'Chris Evans', 'Chris Hemsworth', 'Scarlett Johansson', 'Mark Ruffalo'],
            release_date = 'April 23, 2015'
        ),
        media.Movie(
            title = 'X-Men: Days of Future Past',
            poster_image_url = 'http://www.movieposterdb.com/posters/14_06/2014/1877832/l_1877832_04aaf850.jpg',
            trailer_youtube_url = 'https://www.youtube.com/watch?v=pK2zYHWDZKo',
            director = 'Bryan Singer',
            actors = ['Hugh Jackman', 'Jennifer Lawrence', 'James McAvoy', 'Michael Fassbender', 'Ian McKellen', 'Patrick Stewart', 'Ellen Page', ' Halle Berry', 'Nicholas Hault', 'Fan Bingbing'],
            release_date = 'May 10, 2014'
        ),
        media.Movie(
            title = 'Pacific Rim',
            poster_image_url = 'http://www.movieposterdb.com/posters/12_12/2013/1663662/l_1663662_8561742a.jpg',
            trailer_youtube_url = 'https://www.youtube.com/watch?v=5guMumPFBag',
            director = 'Guillermo del Toro',
            actors = ['Charlie Hunnam' 'Rinko Kikuchi', 'Idris Elba', 'Charlie Day', 'Ron Perlman', 'Robery Kazinsky'],
            release_date = 'July 2, 2013'
        )
    ]

    #create the webpage dynamically
    ft.open_movies_page(movies)

if __name__ == '__main__':
    main()
