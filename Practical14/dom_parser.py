import xml.dom.minidom as minidom
import time

start_time = time.time() # Starting the clock

# Reading XML files
doc = minidom.parse("go_obo.xml") # Parsing XML files with minidom
terms = doc.getElementsByTagName("term") # Get all <term> elements

# term for recording the maximum number of is_a
max_is_a = {
    "molecular_function": (None, "", 0),  # (term_id, term_name, is_a_count)
    "biological_process": (None, "", 0),
    "cellular_component": (None, "", 0)
} # Initialise a dictionary max_is_a for: molecular_function, biological_process, cellular_component, with each value being (term_id, term_name, is_a_count)

# Iterate over all terms
for term in terms:
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    term_name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue # Extracts the term's ID, name, and namespace

    is_a_list = term.getElementsByTagName("is_a")
    is_a_count = len(is_a_list)

    if namespace in max_is_a:
        if is_a_count > max_is_a[namespace][2]:
            max_is_a[namespace] = (term_id, term_name, is_a_count) # If the term belongs to one of the three namespaces and it has a larger is_a: update the corresponding record in max_is_a


# Print results
for ns, (tid, tname, count) in max_is_a.items():
    print(f"\nNamespace: {ns}")
    print(f"  ID: {tid}")
    print(f"  Name: {tname}")
    print(f"  Number of is_a: {count}") # Iterate over max_is_a and print information about the term with the most is_a in each ontology type

end_time = time.time()
print(f"\nDOM parsing took {end_time - start_time:.4f} seconds.")
# DOM is slower than SAX because it loads the entire document into memory
