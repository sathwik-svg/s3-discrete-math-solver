import streamlit as st
import math
import itertools

st.set_page_config(
    page_title="Discrete Math Solver",
    page_icon="🧮",
    layout="wide"
)

st.title("🧮 Discrete Mathematics Solver")
st.caption("S3-P1 • Interactive Discrete Mathematics Toolkit")

st.sidebar.header("📚 Topics")

topic = st.sidebar.selectbox(
    "Choose a topic",
    [
        "Set Operations",
        "Permutations & Combinations",
        "GCD & LCM",
        "Relations",
        "Cartesian Product",
        "Boolean Logic",
        "Truth Table",
        "Graph Theory"
    ]
)

# ---------------- SET OPERATIONS ----------------

if topic == "Set Operations":

    st.header("🔢 Set Operations")

    col1, col2 = st.columns(2)

    with col1:
        a_input = st.text_input(
            "Set A",
            "1,2,3,4"
        )

    with col2:
        b_input = st.text_input(
            "Set B",
            "3,4,5,6"
        )

    try:
        A = set(int(x.strip()) for x in a_input.split(",") if x.strip())
        B = set(int(x.strip()) for x in b_input.split(",") if x.strip())

        st.subheader("Results")

        c1, c2, c3 = st.columns(3)

        c1.metric("A ∪ B", str(sorted(A | B)))
        c2.metric("A ∩ B", str(sorted(A & B)))
        c3.metric("A − B", str(sorted(A - B)))

        st.write("**B − A:**", sorted(B - A))
        st.write("**Symmetric Difference:**", sorted(A ^ B))

        st.write("**A ⊆ B:**", A.issubset(B))
        st.write("**B ⊆ A:**", B.issubset(A))

    except ValueError:
        st.error("Please enter valid integers separated by commas.")


# ---------------- PERMUTATIONS ----------------

elif topic == "Permutations & Combinations":

    st.header("🔀 Permutations & Combinations")

    n = st.number_input(
        "Enter n",
        min_value=0,
        max_value=100,
        value=5,
        step=1
    )

    r = st.number_input(
        "Enter r",
        min_value=0,
        max_value=100,
        value=2,
        step=1
    )

    if r <= n:

        permutation = math.factorial(n) // math.factorial(n - r)
        combination = math.factorial(n) // (
            math.factorial(r) * math.factorial(n - r)
        )

        c1, c2 = st.columns(2)

        c1.metric("nPr", permutation)
        c2.metric("nCr", combination)

    else:
        st.error("r must be less than or equal to n.")


# ---------------- GCD LCM ----------------

elif topic == "GCD & LCM":

    st.header("➗ GCD & LCM Calculator")

    numbers = st.text_input(
        "Enter numbers",
        "12,18,24"
    )

    try:

        nums = [
            int(x.strip())
            for x in numbers.split(",")
            if x.strip()
        ]

        if nums:

            gcd_value = nums[0]

            for number in nums[1:]:
                gcd_value = math.gcd(gcd_value, number)

            lcm_value = nums[0]

            for number in nums[1:]:
                lcm_value = abs(lcm_value * number) // math.gcd(
                    lcm_value,
                    number
                )

            c1, c2 = st.columns(2)

            c1.metric("GCD", gcd_value)
            c2.metric("LCM", lcm_value)

    except ValueError:
        st.error("Enter valid integers.")


# ---------------- RELATIONS ----------------

elif topic == "Relations":

    st.header("🔗 Relation Analyzer")

    relation_input = st.text_area(
        "Enter ordered pairs",
        "(1,1),(1,2),(2,2)"
    )

    try:

        pairs = []

        for item in relation_input.split("),"):
            item = item.replace("(", "").replace(")", "").strip()

            if item:
                x, y = item.split(",")
                pairs.append((int(x), int(y)))

        relation = set(pairs)

        st.write("**Relation:**", sorted(relation))

        domain = sorted(set(x for x, y in relation))
        range_set = sorted(set(y for x, y in relation))

        st.write("**Domain:**", domain)
        st.write("**Range:**", range_set)

        elements = sorted(set(domain + range_set))

        reflexive = all((x, x) in relation for x in elements)

        symmetric = all(
            (y, x) in relation
            for x, y in relation
        )

        st.write("**Reflexive:**", reflexive)
        st.write("**Symmetric:**", symmetric)

    except Exception:
        st.error("Use format like: (1,1),(1,2),(2,2)")


# ---------------- CARTESIAN PRODUCT ----------------

elif topic == "Cartesian Product":

    st.header("✖️ Cartesian Product")

    A_input = st.text_input("Set A", "1,2")
    B_input = st.text_input("Set B", "a,b")

    A = [
        x.strip()
        for x in A_input.split(",")
        if x.strip()
    ]

    B = [
        x.strip()
        for x in B_input.split(",")
        if x.strip()
    ]

    product = list(itertools.product(A, B))

    st.write("### A × B")

    st.write(product)

    st.metric(
        "|A × B|",
        len(product)
    )


# ---------------- BOOLEAN LOGIC ----------------

elif topic == "Boolean Logic":

    st.header("🧠 Boolean Logic")

    A = st.checkbox("A", value=True)
    B = st.checkbox("B", value=False)

    st.subheader("Logical Results")

    c1, c2, c3 = st.columns(3)

    c1.metric("A AND B", A and B)
    c2.metric("A OR B", A or B)
    c3.metric("NOT A", not A)

    st.write("**A XOR B:**", A ^ B)
    st.write("**A → B:**", (not A) or B)
    st.write("**A ↔ B:**", A == B)


# ---------------- TRUTH TABLE ----------------

elif topic == "Truth Table":

    st.header("📊 Boolean Truth Table")

    rows = []

    for A in [False, True]:

        for B in [False, True]:

            rows.append(
                {
                    "A": A,
                    "B": B,
                    "A AND B": A and B,
                    "A OR B": A or B,
                    "A XOR B": A ^ B,
                    "A → B": (not A) or B,
                    "A ↔ B": A == B
                }
            )

    st.dataframe(
        rows,
        use_container_width=True
    )


# ---------------- GRAPH THEORY ----------------

elif topic == "Graph Theory":

    st.header("🕸️ Graph Theory Analyzer")

    vertices = st.number_input(
        "Number of vertices",
        min_value=0,
        max_value=1000,
        value=5
    )

    edges = st.number_input(
        "Number of edges",
        min_value=0,
        max_value=10000,
        value=4
    )

    st.subheader("Graph Properties")

    c1, c2 = st.columns(2)

    c1.metric("Vertices", vertices)
    c2.metric("Edges", edges)

    if vertices > 1:
        max_edges = vertices * (vertices - 1) // 2

        st.write(
            f"Maximum edges in a simple undirected graph: **{max_edges}**"
        )

        if edges <= max_edges:
            st.success("Valid simple undirected graph.")
        else:
            st.error("Too many edges for a simple undirected graph.")

    else:
        st.info("Add at least 2 vertices.")

st.divider()

st.caption(
    "S3 Discrete Math Solver • Built with Python + Streamlit"
)
