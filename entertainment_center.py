import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg' ,
                        'A toy story picture' ,
                        'https://www.youtube.com/watch?v=4KPTXpQehio');
    
#print(toy_story.storyline);

avatar = media.Movie('Avatar',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                     'A marine on an alien planet',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY');

#print(avatar.storyline);

school_of_rock = media.Movie('School of Rock',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg',
                     'School of Rock story',
                     'https://www.youtube.com/watch?v=5afGGGsxvEA');

#print (school_of_rock.storyline);


two_states = media.Movie('2 States',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/1/12/2_States_poster.jpg/220px-2_States_poster.jpg',
                     'The story of two states',
                     'https://www.youtube.com/watch?v=CGyAaR2aWcA');

#print (2_states.storyline);
#2_states.show_trailer();

almost_famous = media.Movie('Almost Famous',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/d/dd/Almost_famous_poster1.jpg/220px-Almost_famous_poster1.jpg',
                     'Almost Famous',
                     'https://www.youtube.com/watch?v=KgjFYmuXbro');

#print (almost_famous.storyline);


princess_diaries = media.Movie('Princess Diaries',
                     'https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Princess_diaries_ver1.jpg/215px-Princess_diaries_ver1.jpg',
                     'Princess Diaries story',
                     'https://www.youtube.com/watch?v=2CkcwPi20ms');

#print (princess_diaries.storyline);

movies = [toy_story, avatar, school_of_rock, two_states, almost_famous, princess_diaries];

fresh_tomatoes.open_movies_page(movies);
