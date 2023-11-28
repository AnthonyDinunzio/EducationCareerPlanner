from pychatsonic.chat import ChatSonic
from flask import Flask, request, render_template


app = Flask(__name__)
chat = ChatSonic("da28b647-1885-48ac-ba0b-c46b7259e1cf", "en")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_location = request.form.get('location')
        user_dob = request.form.get('dob')
        user_hobbies = request.form.get('hobbies')
        user_goals = request.form.get('goals')
        user_achievements = request.form.get('achievements')

        # Pass user information to the AI model
        ai_response = get_ai_response(user_location, user_dob, user_hobbies, user_goals, user_achievements)

        # Render the response template with AI's response
        return render_template('response.html', response=ai_response)

    return render_template('index.html')


def get_ai_response(location, dob, hobbies, goals, achievements):

    user_input = f"My location is {location}, My date of birth is {dob}, my hobbies are {hobbies}, my goals are {goals}" \
                 f"my achievements are {achievements}. Given the information provided can you select a career path for" \
                 f"me then create a fully customized" \
                 f"and comprehensive education and career plan that will get me to that career path? " \
                 f"The plan should include what classes and courses" \
                 f"I will need to reach my career. The plan should also layout what grades I will need and what extra" \
                 f"caricullar activities will be helpful in reaching my career. Then can you explain the plan on" \
                 f"breaking into the industry. The plan should go from beginning of " \
                 f"high school to full time sustainable" \
                 f"career."

    text = chat.ask(user_input)
    return text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
