"""Implementation od the StudentFileReader ADT using a text file as the input source
in which each field is stored on a separate line."""


class StudentFileReader:
    """Create a new student reader instance."""
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    def open(self):
        """Open a connection to the input file."""
        self._inputFile = open(self._inputSrc, "r")

    def close(self):
        """Close a connection to the input file."""
        self._inputFile.close()
        self._inputFile = None

    def fetchAll(self):
        """Extract all student records and store them in a list."""
        theRecords = list()
        student = self.fetchRecord()
        while student is not None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    def fetchRecord(self):
        """Extract the next student record from the file."""

        # Read the first line of the record.
        line = self._inputFile.readline()
        if line == "":
            return None

        # If there is another record, create a storage object and fill it.
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student


class StudentRecord:
    """Storage class used for an individual student record."""
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
