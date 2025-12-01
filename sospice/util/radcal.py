# Rewritten in python from the Spice data analysis tool in IDL (T. Fredvik)
from astropy.io import fits
import re


def _get_radcal_column_number(header_l2: fits.header, binary_table: fits.BinTableHDU):
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
    positive integer

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
    radcal_ttype_list = re.finall('RADCAL' + '.+', radcal_extname_and_ttype)
    if len(radcal_ttype_list) != 1:
        raise KeyError("radcal ttype could not be found in the VAR_KEYS keyword value.")
    radcal_ttype = radcal_ttype_list[0]

    











# FUNCTION get_radcal_column_no, L2_header, lun
#   var_keys = fxpar(L2_header,'VAR_KEYS')
#   radcal_extname = var_keys.extract('.+\;')
#   radcal_extname = radcal_extname.remove(-1)
  
#   radcal_extname_and_ttype = var_keys.extract(radcal_extname+'.+')
#   radcal_ttype = trim(radcal_extname_and_ttype.extract('RADCAL'+'.+'))
    
#   fxbfind, lun, 'TTYPE', column, ttype_value, n_found  
#   radcal_column_ix = where(ttype_value EQ radcal_ttype)
#   column_no = column[radcal_column_ix]
  
#   return, column_no
# END


# FUNCTION get_radcal_exten_no, l2_filename
#   fits_open,l2_filename,fcb
#   fits_close,fcb
  
#   radcal_extname = 'VARIABLE_KEYWORDS'
  
#   radcal_exten_no = where(fcb.extname EQ radcal_extname)
  
#   return, radcal_exten_no
# END


# FUNCTION get_radcal_array, l2_file, exten_no, scalar_value=scalar_value
#   !null = readfits(l2_file,l2_header,exten_no=exten_no)
  
#   radcal_exten_no = get_radcal_exten_no(l2_file)
#   fxbopen,lun, l2_file, radcal_exten_no, radcal_header
  
#   radcal_column_no = get_radcal_column_no(L2_header, lun)
  
#   fxbread, lun, aRadCal, radcal_column_no,1
#   free_lun,lun
  
#   scalar_value = fxpar(l2_header,'RADCAL')
#   return, aRadCal
# END
