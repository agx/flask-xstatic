import flask_xstatic_files as fx


def test_url_for(app):
    xsf = fx.XStaticFiles(app)
    with app.test_request_context():
        assert xsf.url_for('jquery', 'jquery.min.js') == '/xstatic/jquery/jquery.min.js'


def test_init_string(app):
    with app.test_request_context():
        app.config['XSTATIC_MODULES'] = 'jquery,d3'
        xsf = fx.XStaticFiles(app)
        assert 2 == len(xsf.modules)
        assert ['d3', 'jquery'] == sorted(xsf.modules.keys())


def test_init_list(app):
    with app.test_request_context():
        app.config['XSTATIC_MODULES'] = ['jquery', 'd3']
        xsf = fx.XStaticFiles(app)
        assert 2 == len(xsf.modules)
        assert ['d3', 'jquery'] == sorted(xsf.modules.keys())


def test_serve(app):
    fx.XStaticFiles(app)

    c = app.test_client()
    resp = c.get('/xstatic/jquery/exist')
    assert resp.status_code == 404

    resp = c.get('/xstatic/jquery/jquery.min.js')
    assert resp.status_code == 200
