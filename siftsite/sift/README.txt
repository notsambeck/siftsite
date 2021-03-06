SIFT is a visual experiment. It has two parts:

1. SIFT systematically generates every possible image
2. A neural network evaluates each image to determine if it is interesting or not. Candidate images are displayed and/or saved to file.

The goal is to answer a question - using brute-force combinatorics, how many images would you have to generate to find one that is indistinguishable from a photograph?

At the beginning of this project (in 2009), it seemed that the needed number of images was impossible. Or, more precisely, that it was ridiculously unlikely that any generated image would have properties we associate with real images.

Given the scale of the numbers involved, the best strategy for answering this question is to start with ‘minimal’ images - the smallest data objects that start to take on the properties of images. Fortunately, with the development of machine learning as a viable technology over the last ~10 years, scientists have started researching closely related questions. One relevant result comes from CIFAR, an academic project that studies computer vision. They have shown that scene recognition is possible with very small images, both by computers and by people. A 32x32 pixel image contains enough information to identify the context of ~90% of cases. This applies to both humans and computers.


SIFT is built with many pre-existing tools, which can be found in requirements.txt. It is not dependent on CUDA, but it will benefit from CUDA / GPU acceleration.

COMMAND LINE INSTALLATION INSTRUCTIONS for Linux 16
(if you are using older Linux or most other OS, you will probably have to specify Python3 and PIP3. If you are using Windows I don't know what will happen.)

0. Install python3, pip, git, and virtualenv globally

1. Clone SIFT2 repository from Github; cd into sift2 directory
git clone https://github.com/thesambeck/sift2
cd sift2

2. Optional: Make virtualenv and activate it (this keeps SIFT dependencies separate from the rest of your system):
virtualenv env
source env/bin/activate

2. Install SIFT requirements (inside virtualenv) for Python 3 using PIP (you may have to type pip3 here)
pip install -r requirements.txt

3. Upgrade Lasagne and Theano to newest versions (Tested with Lasagne-0.2.dev1 and Theano-0.9.0; this works as of 5/3/17):
pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip

4. Optional: Edit parameters to your liking:
DEFINITELY CHANGE: increment - I have been running 999 as increment, so use a different number.
You can change easily: screen size, save prefs, the range of the transform generator function (i.e. contrast)

5. Run SIFT (visualized or not) in Python 3:
python sift.py
OR
python sift-nonvisual.py



This should get you started. Tools are included in dataset.py to build new neural nets or attempt to improve the existing models.
