'''Photo analyzer to squeeze meaningful metrics from the photo'''

from pathlib import Path

class PhotoAnalyzer:
    '''Photo Analyzer class to analyzer the given photo.'''
    def __init__(self):
        pass

    def calculate_calories(self, photo_url: str):
        '''Calculates calories from the photo url.
        
        Args:
            photo_url: the photo url which can be local or remote storage.

        Returns:
            Bytes of the photo.

        Raises
            NotImplementedError: remote storage is not supported for now.
        '''
        local_path = Path(photo_url)
        
        if local_path.exists():
            self._calculate_calories()
            # TODO(kimnamgue): Calculate calories from the photo using ML.

            return local_path.read_bytes()
        else:
            raise NotImplementedError

    def _calculate_calories(self):
        pass
