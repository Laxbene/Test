import streamlit as st

# Spielfeldgröße
WIDTH = 10
HEIGHT = 6

# Spielzustand speichern
if "x" not in st.session_state:
    st.session_state.x = 0
    st.session_state.y = HEIGHT - 1
    st.session_state.won = False

x = st.session_state.x
y = st.session_state.y

goal_x = WIDTH - 1
goal_y = HEIGHT - 1

st.title("🕹️ Jump and Run – Streamlit")

st.write("Steuerung: Links / Rechts / Springen")

# Steuerungsbuttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Links") and x > 0:
        x -= 1

with col2:
    if st.button("⬆️ Springen") and y > 0:
        y -= 1

with col3:
    if st.button("➡️ Rechts") and x < WIDTH - 1:
        x += 1

# Schwerkraft
if y < HEIGHT - 1:
    y += 1

# Gewonnen?
if x == goal_x and y == goal_y:
    st.session_state.won = True

# Zustand speichern
st.session_state.x = x
st.session_state.y = y

# Spielfeld anzeigen
for row in range(HEIGHT):
    line = ""
    for col in range(WIDTH):
        if col == x and row == y:
            line += "🧍"
        elif col == goal_x and row == goal_y:
            line += "🏁"
        else:
            line += "⬜"
    st.write(line)

if st.session_state.won:
    st.success("🎉 GEWONNEN!")

