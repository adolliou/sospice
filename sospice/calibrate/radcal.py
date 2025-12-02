# Rewritten in python from the Spice data analysis tool in IDL (T. Fredvik)
from astropy.io import fits
import re
from astropy.wcs import WCS
import numpy as np



def _get_radcal_ttype(header_l2: fits.header):
    """
    Return the column number of the radiometric calibration in the
    binary table corresponding to the given FITS HDU header. 

    Parameters
    ----------
    header_l2: fits.header
        header of the HDU L2 fits file
    binary_table: tuple
        Range of base-10 logarithm of temperature, in K
  
    Return
    ------
    ttype of the radcal array on the binary table corresponding to the input header

    """    
    var_keys = header_l2["VAR_KEYS"]
    radcal_extname_list = re.findall('.+;', var_keys)
    if len(radcal_extname_list) != 1:
        raise KeyError("radcal extension name could not be found in the VAR_KEYS keyword value.")
    
    radcal_extname = radcal_extname_list[0][:-1]
    radcal_extname_and_ttype_list = re.findall(radcal_extname + '.+', var_keys)
    if len(radcal_extname_and_ttype_list) != 1:
        raise KeyError("radcal extension and ttype could not be found in the VAR_KEYS keyword value.")
    
    radcal_extname_and_ttype = radcal_extname_and_ttype_list[0]
    radcal_ttype_list = re.findall('RADCAL' + '.+', radcal_extname_and_ttype)
    if len(radcal_ttype_list) != 1:
        raise KeyError("radcal ttype could not be found in the VAR_KEYS keyword value.")
    radcal_ttype = radcal_ttype_list[0]
    return radcal_ttype





def get_radcal_from_hdus(hdu: fits.ImageHDU, hdu_binary: fits.BinTableHDU, return_base_wavelength: bool=False):

    #TODO assert hdu to be for a spectral window.

    radcal_ttype    = _get_radcal_ttype(hdu.header)
    radcal_array    = np.squeeze(hdu_binary.data[radcal_ttype])
    if return_base_wavelength:
        w = WCS(hdu.header)
        w_spec = w.spectral
        x = np.arange(hdu.data.shape[1])
        wavelength_array = w_spec.pixel_to_world(x)
        return radcal_array, wavelength_array
    else:
        return radcal_array





# if __name__ == "__main__":
#     url = ("https://spice.osups.universite-paris-saclay.fr/spice-data/"
#     "release-5.0/level2/2022/04/02/solo_L2_spice-n-ras_20220402T111537_V22_100664002-000.fits")
#     with fits.open(url) as hdul:
#         hdu = hdul[0]
#         hdu_bin = hdul["VARIABLE_KEYWORDS"]

#         get_radcal_from_hdus(hdu, hdu_bin)

