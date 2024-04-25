import streamlit as st


# 
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)

custom_css = """
    <style>
        h1{
            text-align: center;
        }
        .container {
            background-color: #f4f4f4;
            border-radius: 5px;
            box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 400px;
            margin: auto;
        }

        .profile-image {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto 20px;
            display: block;
        }

        .btext {
            font-size: 22px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }

        .social-links {
            display: flex;
            justify-content: center;
        }

        .social-links a {
            text-decoration: none;
            color: #007bff;
            margin: 0 10px;
            font-size: 24px;
        }

    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# My Profile --------------------------------------------------------------------------------------
profile_Info = """
    <h1>My profile:</h1>
    <div class="container">
        <img class="profile-image" src="https://avatars.githubusercontent.com/u/10818731?s=400&u=0428380ca432f40f3ec916849ba2ca7c780fe889&v=4" alt="User Image" />
        <div class="btext">Mohsen Saadatpour Moghaddam</div>
        <div class="btext">Università degli studi di Verona</div>
        <div class="btext">Year: 2023/2024</div>
        <div class="">mohsen.saadatpourmoghaddam@studenti.univr.it</div>
        <div class="social-links">
            <a href="https://linkedin.com/in/mohsen-saadatpour-5b5a395b" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/mohsen990" target="_blank"><i class="fab fa-github"></i></a>
        </div>
        
    </div>
"""

st.markdown(profile_Info, unsafe_allow_html=True)