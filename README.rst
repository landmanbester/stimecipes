stimecipes is a collection of unsorted stimela cabs and recipes. Use at your own peril!

27 March commands
=================


Install apptainer with suid
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the ppa:

.. code:: bash

  sudo add-apt-repository -y ppa:apptainer/ppa
  sudo apt update

To remove apptainer from your system, run the following command:

.. code:: bash

  sudo apt purge apptainer

Now remove stray files:

.. code:: bash 

  sudo apt autoremove 

Check if any files are left:

.. code:: bash

  whereis apptainer

Follow the same steps for singularity in case it is installed.

Install with suid using the following command:

.. code:: bash

  sudo apt install apptainer-suid

Check if the installation was successful:

.. code:: bash

  ls -la $(which apptainer)

Make a ``.singularity`` directory in your home directory:

.. code:: bash

  mkdir ~/.singularity

And make sure it has the correct permissions:

.. code:: bash

  chmod 700 ~/.singularity


Install ``refactor-0.2.0`` branch of ``cult-cargo`` package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new virtual environment to be safe.
It is best to do this in a new directory (suggest using something like ``~/.venv`` for all virtual environments).

.. code:: bash

  python3 -m venv ccargo2
  source ccargo2/bin/activate
  pip install --upgrade pip wheel 'setuptools[core]'

Now install the package:

.. code:: bash

  pip install git+https://github.com/caracal-pipeline/cult-cargo.git


Get recipes and cabs
~~~~~~~~~~~~~~~~~~~~

We'll be using the ``nassp`` branch of the ``stimecipes`` repository.
Clone the repository with the following command and change into the directory:

.. code:: bash

  git clone --single-branch --branch nassp https://github.com/landmanbester/stimecipes.git
  cd stimecipes

We'll do all our experiments in here for now. Please do not push back to the branch.

Downloading test data
~~~~~~~~~~~~~~~~~~~~~

Download the test data from the following link:

`Test data <https://drive.google.com/file/d/1ONW5JtDbz5-0fjxgG0e-By5RYUfYNkRy/view?usp=sharing>`_

Extract the data into a subdirectory called `msdir` in the `stimecipes` directory:

.. code:: bash

  mkdir msdir
  tar -xvf /path/to/ARIWS.INTROFIMAGING.TriA.1559937657.tar.gz -C msdir

Running stimela
~~~~~~~~~~~~~~~

Since all the paths are hardcoded in this recipe you should now be able to run the recipe with

.. code:: bash

  stimela run triA.yaml