import streamlit as st
from pathlib import Path

# Allama Iqbal Biography Web Application
# Created with Python
# Created by: Masooma Batool

st.set_page_config(
    page_title="Allama Iqbal Biography",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ALLAMA MUHAMMAD IQBAL")
st.subheader("شاعرِ مشرق | مفکرِ پاکستان")
st.caption("A Complete Biography and Literary Collection")

st.sidebar.title("📖 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home", "Biography", "Education", "Career", "Income",
        "Books", "Poetry", "Ghazals", "Famous Poems",
        "Achievements", "Pakistan Movement", "Gallery", "References"
    ]
)

photo = Path("iqbal.jpg")

if page == "Home":
    st.header("Welcome to Allama Iqbal Website")
    if photo.exists():
        st.image(str(photo), width=300)
    else:
        st.info("Place Allama Iqbal's portrait in the project folder with the name iqbal.jpg")

    st.title("Dr. Allama Muhammad Iqbal")
    st.write("""
    Allama Muhammad Iqbal was a famous poet, philosopher,
    lawyer and political thinker.

    He is known as the Poet of the East. His poetry gives
    the message of self-respect, courage, knowledge and hard work.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Birth Year", "1877")
    col2.metric("Death Year", "1938")
    col3.metric("Birth Place", "Sialkot")
    st.info("Website Created by: Masooma Batool")

elif page == "Biography":
    st.header("Complete Biography")
    st.write("""
    Allama Muhammad Iqbal was born on 9 November 1877 in Sialkot.
    His father was Sheikh Noor Muhammad and his mother was Imam Bibi.

    He was a great Urdu and Persian poet, philosopher, lawyer and
    political thinker. His poetry teaches the lesson of Khudi,
    courage, knowledge and self-respect.

    He died on 21 April 1938 in Lahore.
    """)

    st.subheader("Personal Information")
    information = {
        "Full Name": "Dr. Sir Muhammad Iqbal",
        "Famous Name": "Allama Iqbal",
        "Date of Birth": "9 November 1877",
        "Birth Place": "Sialkot",
        "Father": "Sheikh Noor Muhammad",
        "Mother": "Imam Bibi",
        "Date of Death": "21 April 1938",
        "Death Place": "Lahore",
        "Profession": "Poet, Philosopher and Lawyer",
        "Languages": "Urdu and Persian"
    }
    for key, value in information.items():
        st.write(f"**{key}:** {value}")

elif page == "Education":
    st.header("Educational History")
    education = [
        "Early education in Sialkot.",
        "Studied under Syed Mir Hassan.",
        "Studied at Scotch Mission College.",
        "Studied at Government College Lahore.",
        "Completed MA in Philosophy in 1899.",
        "Studied at Trinity College Cambridge.",
        "Obtained PhD from Munich University in 1907.",
        "Qualified in Law from Lincoln's Inn in 1908."
    ]
    for item in education:
        st.write("🎓", item)

elif page == "Career":
    st.header("Career and Profession")
    st.write("""
    Allama Iqbal worked in different fields:
    1. Urdu and Persian Poet
    2. Philosopher
    3. Lawyer
    4. Teacher
    5. Political Thinker
    6. Writer
    7. Scholar

    He practiced law in Lahore and also worked as a teacher.
    """)

elif page == "Income":
    st.header("Income and Sources of Income")
    st.write("""
    There is no reliable, verified public record of Allama Iqbal's
    exact total income or wealth.

    His known professional sources of income included:
    """)
    for source in ["Law Practice", "Teaching", "Writing and Literary Work", "Books and Publications"]:
        st.write("💰", source)
    st.warning("Exact salary, monthly income and total wealth are not confirmed. No invented figures are shown.")

elif page == "Books":
    st.header("Famous Books of Allama Iqbal")
    books = [
        ("Asrar-e-Khudi", "1915", "Persian"),
        ("Rumuz-e-Bekhudi", "1918", "Persian"),
        ("Payam-e-Mashriq", "1923", "Persian"),
        ("Bang-e-Dara", "1924", "Urdu"),
        ("Zabur-e-Ajam", "1927", "Persian"),
        ("Javid Nama", "1932", "Persian"),
        ("Bal-e-Jibril", "1935", "Urdu"),
        ("Pas Cheh Bayad Kard", "1936", "Persian"),
        ("Zarb-e-Kalim", "1936", "Urdu"),
        ("Musafir", "1936", "Persian"),
        ("Armaghan-e-Hijaz", "1938", "Urdu and Persian")
    ]
    for number, (name, year, language) in enumerate(books, 1):
        with st.expander(f"{number}. {name}"):
            st.write("Publication Year:", year)
            st.write("Language:", language)
    st.info("These are 11 major poetry collections. Iqbal also wrote prose books and other works.")

elif page == "Poetry":
    st.header("Allama Iqbal Poetry")
    st.write("""
    Allama Iqbal wrote poetry mainly in Urdu and Persian.

    His poetry teaches:
    - Khudi (Self-respect)
    - Love of knowledge
    - Courage
    - Unity
    - Hard work
    - Faith
    """)
    st.subheader("Famous Poetry Collections")
    for item in ["Bang-e-Dara", "Bal-e-Jibril", "Zarb-e-Kalim", "Asrar-e-Khudi", "Javid Nama", "Zabur-e-Ajam"]:
        st.write("✒️", item)

elif page == "Ghazals":
    st.header("Famous Ghazals and Poetry")
    ghazals = [
        "ستاروں سے آگے جہاں اور بھی ہیں",
        "نہیں تیرا نشیمن قصر سلطانی کے گنبد پر",
        "دل سے جو بات نکلتی ہے اثر رکھتی ہے",
        "خودی کو کر بلند اتنا",
        "نگاہ بلند سخن دل نواز جاں پرسوز"
    ]
    for item in ghazals:
        st.write("✒️", item)
    st.caption("These are famous poetic lines, not a verified complete list of Iqbal's ghazals.")

elif page == "Famous Poems":
    st.header("Famous Poems of Allama Iqbal")
    poems = [
        "Shikwa", "Jawab-e-Shikwa", "Masjid-e-Qurtuba",
        "Tarana-e-Hindi", "Tarana-e-Milli", "Lab Pe Aati Hai Dua",
        "Tulu-e-Islam", "Himalaya", "Saqi Nama", "Khizr-e-Rah"
    ]
    for number, poem in enumerate(poems, 1):
        st.write(f"{number}. {poem}")

elif page == "Achievements":
    st.header("Awards and Achievements")
    achievements = [
        "Recognized as Pakistan's National Poet.",
        "Known as Poet of the East.",
        "Received the title of Sir in 1922.",
        "Earned a PhD from Munich University.",
        "Became a famous Urdu and Persian poet.",
        "Presented the Allahabad Address in 1930.",
        "His poetry inspired generations."
    ]
    for item in achievements:
        st.write("🏆", item)

elif page == "Pakistan Movement":
    st.header("Contribution to Pakistan Movement")
    st.write("""
    Allama Iqbal played an important role in the political thinking
    of Muslims of the Indian subcontinent.

    In December 1930, he delivered his famous Allahabad Address.
    He presented the idea of a separate political future for Muslims
    in the northwestern regions of the subcontinent.

    His ideas later became an important part of the intellectual
    background of Pakistan.
    """)

elif page == "Gallery":
    st.header("Allama Iqbal Photo Gallery")
    if photo.exists():
        st.image(str(photo), caption="Allama Muhammad Iqbal", width=400)
    else:
        st.warning("Please add iqbal.jpg in the project folder.")
    st.write("Photo credit: Use a properly sourced historical portrait.")

elif page == "References":
    st.header("Research and References")
    st.write("For further information, visit:")
    st.markdown("[Official Allama Iqbal Website](https://www.allamaiqbal.com)")
    st.markdown("[Iqbal Academy Pakistan](https://www.iap.gov.pk)")
    st.markdown("[International Iqbal Society](https://www.iqbal.com.pk)")
    st.write("Information in this application is provided for educational purposes.")

st.divider()
st.caption("Allama Iqbal Biography Web Application | Created by Masooma Batool")
st.caption("Made with Python and Streamlit")
