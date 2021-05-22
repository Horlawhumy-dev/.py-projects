from main import Question

question_prompt = [
    "1. How many types of head tags is in html? \n(a) 6\n(b) 5\n(c) uncountabel\n(d) none\n\n",

    "2. The code to upload image in html is? \n(a) <img src alt=> \n(b) img src= alt> \n(c) <img src="" alt=""> "
    "\n(d) <img  alt="">\n\n",

    "3. To make any of the selected element a link, which of the tags do we make use of? \n(a) body \n(b) img "
    "\n(c) anchor \n(d) iframe\n\n",

    "4. The tag used to connect external css files to html file is called? \n(a)connector \n(b) link "
    "\n(c) anchor \n(d)script \n\n",

    "5. The following is not the among language needed for the structuring, styling and making website rexponsive? "
    "\n(a)Java \n(b) JavaScript \n(c) CSS \n(d)None \n\n",

    "6. Which of these editors is not useful for making website pages in browsers? \n(a)Sublime \n(b)Atom \n(c)Note++ "
    "\n(d)Eclipse \n\n",

    "7. The full meaning to the styling sheet of web languages is? \n(a)Cascarding Style Sheet "
    "\n(b)Canadian Style Sheet" " \n(c)Cascading Styles \n(d) None \n\n",
]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "c"),
    Question(question_prompt[3], "b"),
    Question(question_prompt[4], "a"),
    Question(question_prompt[5], "d"),
    Question(question_prompt[6], "d"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Congratulations! You got " + str(score) + "/" + str(len(questions)) + " correctly")


run_test(questions)