#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmcaddon

ADDON = xbmcaddon.Addon(id = 'script.moviequiz')

Q_WHAT_MOVIE_IS_THIS = 30400
Q_WHAT_MOVIE_IS_ACTOR_NOT_IN = 30401
Q_WHAT_YEAR_WAS_MOVIE_RELEASED = 30402
Q_WHAT_TAGLINE_BELONGS_TO_MOVIE = 30403
Q_WHO_DIRECTED_THIS_MOVIE = 30404
Q_WHAT_STUDIO_RELEASED_MOVIE = 30405
Q_WHAT_ACTOR_IS_THIS = 30406
Q_WHO_PLAYS_ROLE_IN_MOVIE = 30407
Q_WHO_VOICES_ROLE_IN_MOVIE = 30408
Q_WHAT_MOVIE_IS_THIS_QUOTE_FROM = 30409
Q_WHAT_MOVIE_IS_THE_NEWEST = 30410
Q_WHAT_MOVIE_IS_NOT_DIRECTED_BY = 30411
Q_WHAT_ACTOR_IS_IN_THESE_MOVIES = 30412
Q_WHAT_ACTOR_IS_IN_MOVIE_BESIDES_OTHER_ACTOR = 30413
Q_WHAT_MOVIE_HAS_THE_LONGEST_RUNTIME = 30414

Q_WHAT_TVSHOW_IS_THIS = 30450
Q_WHAT_SEASON_IS_THIS = 30451
Q_WHAT_EPISODE_IS_THIS = 30452
Q_WHEN_WAS_EPISODE_FIRST_AIRED = 30453
Q_WHEN_WAS_TVSHOW_FIRST_AIRED = 30454
Q_WHO_PLAYS_ROLE_IN_TVSHOW = 30455
Q_WHO_VOICES_ROLE_IN_TVSHOW = 30456
Q_WHAT_TVSHOW_IS_THIS_QUOTE_FROM = 30457
Q_WHAT_TVSHOW_IS_THIS_THEME_FROM = 30458

Q_SPECIALS = 30005
Q_SEASON_NO = 30006
Q_FIRST_AIRED_DATEFORMAT = 30007

G_QUESTION_X_OF_Y = 30000
G_GAME_OVER = 30003
G_YOU_SCORED = 30004
G_ADD_USER = 30015
G_WELCOME_ENTER_NICKNAME = 30010

G_X_QUESTIONS_LEFT = 30133
G_LAST_QUESTION = 30134
G_X_MINUTES_LEFT = 30135

M_MOVIE_COLLECTION_TRIVIA = 30110
M_MOVIE_COUNT = 30111
M_ACTOR_COUNT = 30112
M_DIRECTOR_COUNT = 30113
M_STUDIO_COUNT = 30114
M_HOURS_OF_ENTERTAINMENT = 30115

M_TVSHOW_COLLECTION_TRIVIA = 30120
M_TVSHOW_COUNT = 30121
M_SEASON_COUNT = 30122
M_EPISODE_COUNT = 30123

M_CHOOSE_MOVIE_GAME_TYPE = 30600
M_CHOOSE_TV_GAME_TYPE = 30601

M_ONE_MINUTE = 30130
M_X_MINUTES = 30131
M_X_QUESTIONS = 30132

S_DOWNLOADING_IMDB_DATA = 30520
S_RETRIEVED_X_OF_Y_MB = 30521
S_FILE_X_OF_Y = 30525
S_DOWNLOAD_COMPLETE = 30526

M_UNLIMITED = 30705
M_X_QUESTIONS_LIMIT = 30706
M_ONE_MINUT_LIMIT = 30707
M_X_MINUTS_LIMIT = 30708

M_STATISTICS = 30820
M_CHOOSE_TYPE = 30815

M_DEVELOPED_BY = 39998
M_TRANSLATED_BY = 39999

E_WARNING = 30050
E_ALL_MOVIE_QUESTIONS_DISABLED = 30051
E_ALL_TVSHOW_QUESTIONS_DISABLED = 30052
E_QUIZ_TYPE_NOT_AVAILABLE = 30053
E_REQUIREMENTS_MISSING = 30054

E_REQUIREMENTS_MISSING_LINE1 = 30055
E_REQUIREMENTS_MISSING_LINE2 = 30056
E_REQUIREMENTS_MISSING_LINE3 = 30057

E_DELETE_USER = 30058
E_DELETE_USER_LINE1 = 30059
E_DELETE_USER_LINE2 = 30060

E_ONLY_WATCHED_LINE1 = 30061
E_ONLY_WATCHED_LINE2 = 30062
E_ONLY_WATCHED_LINE3 = 30063

E_MOVIE_RATING_LIMIT_LINE1 = 30064
E_MOVIE_RATING_LIMIT_LINE2 = 30065
E_MOVIE_RATING_LIMIT_LINE3 = 30066

E_TVSHOW_RATING_LIMIT_LINE1 = 30067
E_TVSHOW_RATING_LIMIT_LINE2 = 30068
E_TVSHOW_RATING_LIMIT_LINE3 = 30069


SETT_ONLY_WATCHED_MOVIES = 'only.watched.movies'
SETT_MOVIE_RATING_LIMIT_ENABLED = 'movie.rating.limit.enabled'
SETT_TVSHOW_RATING_LIMIT_ENABLED = 'tvshow.rating.limit.enabled'

def strings(id, replacements = None):
    string = ADDON.getLocalizedString(id)
    if replacements is not None:
        return string % replacements
    else:
        return string