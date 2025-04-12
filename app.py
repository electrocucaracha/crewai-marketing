# Copyright (c) 2025
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Provides an application for generating a LinkedIn post
"""

import streamlit as st
from marketing.crew import Marketing

st.title("LinkedIn post generator")

idea = st.text_area("Main idea:")
if st.button("Generate"):
    try:
        with st.spinner("Processing idea...", show_time=True):
            result = Marketing().crew().kickoff(inputs={"idea": idea})
        st.markdown(result.raw)
        st.success("Done!")
    except Exception as e:
        raise ValueError("An error occurred while running the Marketing crew") from e
