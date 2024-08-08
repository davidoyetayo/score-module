from utils import scores_file_name, bad_return_code
import os

def add_score(difficulty):
    try:
        points_of_winning = (difficulty * 3) + 5
        if os.path.exists(scores_file_name):
            with open(scores_file_name, 'r') as file:
                current_score = int(file.read())
        else:
            current_score = 0

        new_score = current_score + points_of_winning

        with open(scores_file_name, 'w') as file:
            file.write(str(new_score))

    except Exception as e:
        print(f'Failed to update score: {e}')
        return bad_return_code
