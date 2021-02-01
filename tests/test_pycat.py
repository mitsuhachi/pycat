import subprocess
import tempfile
import unittest


class TestCommandLineInterface(unittest.TestCase):

    def test_read_files(self):
        """Test concatenation of files"""
        with tempfile.NamedTemporaryFile() as first_file:
            with tempfile.NamedTemporaryFile() as second_file:
                first_file.write('line in first file'.encode('utf-8'))
                first_file.flush()
                second_file.write('line in second file'.encode('utf-8'))
                second_file.flush()

                process = subprocess.run(
                    ['python', '-m', 'pycat', first_file.name, second_file.name],
                    stdout=subprocess.PIPE,
                    universal_newlines=True
                )

                self.assertEqual(0, process.returncode)
                self.assertEqual('line in first file\nline in second file\n', process.stdout)
