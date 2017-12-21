Flask-XStatic-Files
===================

.. image:: https://travis-ci.org/agx/flask-xstatic-files.svg?branch=master
    :target: https://travis-ci.org/agx/flask-xstatic-files

.. highlight:: python

A `Flask`_ extionsion to serve `XStatic`_ files. Can be useful if you
don't use an asset pipeline and want to serve e.g. XStatic packaged
javascript files like `JQuery`_ directly.

Setup
-----
Upon initialization tell Flask about the XStatic modules you want to
use. This example uses JQuery and D3::

    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config.['XSTATIC_MODULES'] = "jquery,d3"
    xsf = XStaticFiles(app)


Serving Files
-------------
Install a minimal route handler to serve the files::

    @app.route('/xstatic/<module>/<path:filename>')
    def xstatic(module, filename):
        return xsf.serve_or_404(module, filename)

In your templates you can then use ``xstatic_url_for``:

.. code-block:: html

    <script type=text/javascript src="{{ xstatic_url_for(module='jquery', path='jquery.min.js') }}"></script>

This has the advantage that you can later serve files from a static
web server by adjusting ``XSTATIC_ROOT`` and ``XSTATIC_PROTO`` without
having to modify any code.

.. _Flask: http://flask.pocoo.org/
.. _XStatic: https://xstatic.readthedocs.io/en/latest/
.. _JQuery: https://pypi.python.org/pypi/XStatic-jQuery
