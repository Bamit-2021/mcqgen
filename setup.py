from setuptools import find_packages,setup

setup(
    name='MCQ Generator',
    version='0.0.1',
    author='B Amit Kumar Patro',
    author_email='patroamit358@gmail.com',
    install_requirements=["openai","langchain","streamlit","python-dotenv","pyPDF2"],
    packages=find_packages()
)