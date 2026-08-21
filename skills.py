SKILLS = [

"python",
"java",
"c",
"c++",
"html",
"css",
"javascript",
"sql",
"mysql",
"mongodb",
"react",
"streamlit",
"django",
"flask",
"git",
"github",
"docker",
"kubernetes",
"aws",
"azure",
"machine learning",
"deep learning",
"nlp",
"pandas",
"numpy",
"tensorflow",
"pytorch"

]

def extract_skills(text):

    found=[]

    text=text.lower()

    for skill in SKILLS:

        if skill in text:

            found.append(skill.title())

    return sorted(list(set(found)))