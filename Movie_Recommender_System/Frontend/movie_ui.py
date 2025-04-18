import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="Movie Recommender 🎬", page_icon="🍿", layout="centered")

st.markdown("""
<style>
/* Full white background everywhere */
html, body, [data-testid="stApp"], [data-testid="stAppViewContainer"],
[data-testid="stSidebar"], [data-testid="stHeader"], .main, .block-container {
    background-color: #ffffff !important;
    color: #111111 !important;
    padding: 0 !important;
}

/* Remove any shadow or residual padding/margins */
.block-container {
    padding: 1rem !important;
}

/* Input box shine */
.stTextInput > div > div > input {
    background-color: #ffffff;
    padding: 12px;
    border-radius: 8px;
    color: #111111;
    border: 2px solid navy;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    width: 100%;  /* Full width for mobile */
}

.stTextInput > div > div > input:hover {
    border-color: #000080;
    box-shadow: 0 0 5px rgba(0, 0, 128, 0.2);
}

.stTextInput > div > div > input:focus {
    outline: none;
    border-color: #000080;
    box-shadow: 0 0 8px rgba(0, 0, 128, 0.3);
}

/* Button */
.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px 20px;
    margin-top: 10px;
    width: 100%;  /* Full width for mobile */
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #45a049;
}

/* Movie card */
.movie-card {
    padding: 10px;
    border-radius: 10px;
    background-color: #f9f9f9;
    margin-bottom: 20px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    width: 100%;  /* Full width for mobile */
}

.movie-card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

.movie-title {
    font-size: 16px;
    font-weight: bold;
    margin-top: 8px;
    color: #222;
}

/* Ensure Movie Card layout is responsive */
@media (max-width: 600px) {
    .movie-card {
        width: 90% !important;  /* Adjust for mobile screens */
        margin: 10px auto !important;  /* Center and add space around */
    }

    .movie-title {
        font-size: 14px !important;
    }
}

/* Movie poster image */
.movie-card img {
    width: 100%;
    max-width: 150px;
    height: auto;
    border-radius: 8px;
    margin-bottom: 10px;
}

/* Desktop Layout Adjustments */
@media (min-width: 601px) {
    .movie-card {
        width: 30% !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.title("🍿 Movie Recommender System")
st.subheader("Get similar movies based on your favorite film 🎥")

# --- Instruction ---
st.info("Enter a movie title below and we'll recommend 5 similar ones!")

# --- User Input ---
movie_name = st.text_input("🔍 Movie Title")

# Always 5 recommendations
top_n = 5

# --- Call Backend ---
if st.button("✨ Recommend"):
    if not movie_name.strip():
        st.warning("⚠️ Please enter a movie title.")
    else:
        response = requests.post(
            "http://backend:8000/recommend",
            json={"title": movie_name, "top_n": top_n}
        )
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                st.error(f"🚫 {data['error']}")
            else:
                st.success("Here are your movie recommendations:")
                
                recommended = data["recommendations"]
                # Use a responsive layout for displaying posters
                cols = st.columns(5)  # Create 5 columns for displaying posters

                for idx, movie in enumerate(recommended):
                    with cols[idx % 5]:  # Distribute the movies across columns
                        poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster']}"
                        st.markdown(f"""
                            <div class="movie-card">
                                <img src="{poster_url}" width="150px">
                                <div class="movie-title">{movie['title']}</div>
                            </div>
                        """, unsafe_allow_html=True)
        else:
            st.error("❌ Server error. Please try again later.")
