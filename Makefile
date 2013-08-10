develop:
	pip install -q "file://`pwd`#egg=django-mailwhimp"
	pip install -q -e .

clean:
	find . -name '*.pyc' | xargs rm -f