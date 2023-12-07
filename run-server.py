#! /usr/bin/env python

from trace_collector import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', ssl_context="adhoc", port=3043)
