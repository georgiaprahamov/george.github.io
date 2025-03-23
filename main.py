from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'Handwritten Digit Recognition',
            'description': 'Application for recognizing handwritten digits (Multilayer Percepton)',
            'technologies': ['Python', 'Keras', 'Tensorflow', 'Matplotlib', 'Numpy'],
            'image': 'handwritting.jpg',
            'link': 'https://github.com/georgiaprahamov/Handwritten-Digit-Classification'
        },
        {
            'title': 'Classic Cryptography',
            'description': 'Application for encrypting and decrypting text using classic cryptography methods',
            'technologies': ['C'],
            'image': 'cryptography.jpeg',
            'link': 'https://github.com/georgiaprahamov/Classic_Cryptography'
        },
        {
            'title': 'Load Repositories',
            'description': 'Web application using AJAX and JQuery',
            'technologies': ['HTML', 'CSS', 'JavaScript', 'AJAX', 'JQuery'],
            'image': 'repos.png',
            'link': 'https://github.com/georgiaprahamov/load-repos'
        }
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
