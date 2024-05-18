import unittest
from unittest.mock import patch, MagicMock
from db.populate_database import load_documents, split_documents, add_to_chroma, calculate_chunk_ids, clear_database

class TestPopulateDatabase(unittest.TestCase):
    @patch('db.populate_database.PyPDFDirectoryLoader')
    def test_load_documents(self, mock_loader):
        mock_loader.return_value.load.return_value = ['doc1', 'doc2']
        result = load_documents()
        self.assertEqual(result, ['doc1', 'doc2'])

    @patch('db.populate_database.RecursiveCharacterTextSplitter')
    def test_split_documents(self, mock_splitter):
        mock_splitter.return_value.split_documents.return_value = ['chunk1', 'chunk2']
        result = split_documents(['doc1', 'doc2'])
        self.assertEqual(result, ['chunk1', 'chunk2'])

    @patch('db.populate_database.Chroma')
    def test_add_to_chroma(self, mock_chroma):
        mock_db = MagicMock()
        mock_chroma.return_value = mock_db
        mock_db.get.return_value = {"ids": []}
        chunks = [MagicMock(), MagicMock()]
        chunks[0].metadata = {"id": "id1"}
        chunks[1].metadata = {"id": "id2"}
        add_to_chroma(chunks)
        mock_db.add_documents.assert_called_once()

    def test_calculate_chunk_ids(self):
        chunks = [MagicMock(), MagicMock()]
        chunks[0].metadata = {"source": "source1", "page": "page1"}
        chunks[1].metadata = {"source": "source1", "page": "page1"}
        result = calculate_chunk_ids(chunks)
        self.assertEqual(result[0].metadata["id"], "source1:page1:0")
        self.assertEqual(result[1].metadata["id"], "source1:page1:1")

    @patch('db.populate_database.os.path')
    @patch('db.populate_database.shutil')
    def test_clear_database(self, mock_shutil, mock_path):
        mock_path.exists.return_value = True
        clear_database()
        mock_shutil.rmtree.assert_called_once()

if __name__ == '__main__':
    unittest.main()