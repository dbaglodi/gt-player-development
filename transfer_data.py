import numpy as np
import pandas as pd

names = np.array(['James Banks III F', 'Bubba Parham G', 'Jordan Usher G', 'Kyle Sturdivant G', 'Rodney Howard F', 'Deivon Smith G', 'Ja\'von Franklin F', 'Lance Terry G'])
years = np.array(['2018', '2019', '2019', '2020', '2020', '2021', '2022', '2022'])
transferred_from = np.array(['University of Texas', 'Virginia Military Institute', 'University of South Carolina', 'University of South Carolina', 'University of Georgia', 'Mississippi State University', 'University of South Alabama', 'Gardner-Webb University'])
games_played_at_prev_school = np.array([46, 62, 48, 21, 24, 33, 28, 54])
games_played_at_gt = np.array([62, 58, 81, 94, 70, 48, 32, 29])
points_scored_at_prev_school = np.array([76, 1125, 274, 43, 31, 173, 29, 598])
points_scored_at_gt = np.array([619, 327, 963, 647, 342, 328, 310, 294])
players = pd.DataFrame({
    'Name': names,
    'Year Joined':years,
    'Previous School': transferred_from,
    'Games Played at Previous School' : games_played_at_prev_school,
    'Games Played at GT': games_played_at_gt,
    'Total Games Played': games_played_at_prev_school + games_played_at_gt,
    'Total Points Scored at Previous School': points_scored_at_prev_school,
    'Total Points Scored at GT': points_scored_at_gt,
    'Total Points Scored': points_scored_at_prev_school + points_scored_at_gt,
    'Average Points per Game at Previous School': points_scored_at_prev_school / games_played_at_prev_school,
    'Average Points per Game at GT': points_scored_at_gt / games_played_at_gt,
    'Average Points per Game': (points_scored_at_prev_school + points_scored_at_gt) / (games_played_at_prev_school + games_played_at_gt)
})