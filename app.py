python3.7 -m venv ~/.streamlit_ve
source ~/.streamlit_ve/bin/activate
pip install -U pip
pip install streamlit
pip install networkx

import time
import base64
import streamlit as st
import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import plotly_express as px
