import xml.sax
import time

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.term_id = ""
        self.term_name = ""
        self.namespace = ""
        self.is_a_count = 0

        self.max_is_a = {
            "molecular_function": ("", "", 0),
            "biological_process": ("", "", 0),
            "cellular_component": ("", "", 0)
        }

        self.inside_term = False
        self.name_buffer = ""  # Create a class GOHandler that inherits from xml.sax.ContentHandler
                               # - Initialize variables to temporarily record information about the current term
                               # - Initialize the max_is_a dictionary to record the term with the highest is_a in the three namespaces

    def startElement(self, name, attrs):
        self.current_element = name
        if name == "term":
            self.inside_term = True
            self.term_id = ""
            self.term_name = ""
            self.namespace = ""
            self.is_a_count = 0
            self.name_buffer = "" # If a <term> is encountered, start recording the new term, resetting the relevant variables.

        if name == "is_a":
            self.is_a_count += 1 # If <is_a> is encountered, add one to the is_a count

    def endElement(self, name):
        if name == "term":
            if self.namespace in self.max_is_a:
                if self.is_a_count > self.max_is_a[self.namespace][2]:
                    self.max_is_a[self.namespace] = (self.term_id, self.term_name, self.is_a_count)
            self.inside_term = False

        if name == "name" and self.inside_term:
            self.term_name = self.name_buffer.strip()
            self.name_buffer = ""

    def characters(self, content):
        if self.current_element == "id" and self.inside_term:
            self.term_id += content.strip()  # If the current element is <id>, record the term ID
        elif self.current_element == "namespace" and self.inside_term:
            self.namespace += content.strip() # If the current element is <namespace>, record namespace
        elif self.current_element == "name" and self.inside_term:
            self.name_buffer += content  # Note that you can't use strip directly, because the name may be passed in as multiple segments.


# Initiate parsing and timing
start_time = time.time() #Start the SAX parser and start the timer

parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml") #Read the XML file with the parser and process the content with the GOHandler

end_time = time.time()

# Print results
for ns, (tid, tname, count) in handler.max_is_a.items():
    print(f"\nNamespace: {ns}")
    print(f"  ID: {tid}")
    print(f"  Name: {tname}")
    print(f"  Number of is_a: {count}") #End the timer and output the result and runtime for each type of namespace in max_is_a
print(f"\nSAX parsing took {end_time - start_time:.4f} seconds.")
# SAX is faster than DOM and suitable for large files
