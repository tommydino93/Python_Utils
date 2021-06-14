import os
import SimpleITK as sitk
import nibabel as nib
from typing import Iterator, Dict, List


def resample_volume(volume_path: str, new_spacing: List, out_path, interpolator=sitk.sitkLinear) -> tuple:
    """This function resamples the input volume to a specified voxel spacing
    Args:
        volume_path (str): input volume path
        new_spacing (list): desired voxel spacing that we want
        out_path (str): path where we temporarily save the resampled output volume
        interpolator (int): interpolator that we want to use (e.g. 1= NearNeigh., 2=linear, ...)
    Returns:
        resampled_volume_sitk_obj (sitk.Image): resampled volume as sitk object
        resampled_volume_nii_obj (nib.Nifti1Image): resampled volume as nib object
        resampled_volume_nii (np.ndarray): resampled volume as numpy array
    """
    volume = sitk.ReadImage(volume_path)  # read volume
    original_size = volume.GetSize()  # extract size
    original_spacing = volume.GetSpacing()  # extract spacing
    new_size = [int(round(osz * ospc / nspc)) for osz, ospc, nspc in zip(original_size, original_spacing, new_spacing)]
    resampled_volume_sitk_obj = sitk.Resample(volume, new_size, sitk.Transform(), interpolator,
                                              volume.GetOrigin(), new_spacing, volume.GetDirection(), 0,
                                              volume.GetPixelID())
    sitk.WriteImage(resampled_volume_sitk_obj, out_path)  # write sitk volume object to disk
    resampled_volume_nii_obj = nib.load(out_path)  # type: nib.Nifti1Image # load volume as nibabel object
    resampled_volume_nii = np.asanyarray(resampled_volume_nii_obj.dataobj)  # type: np.ndarray # convert from nibabel object to np.array
    os.remove(out_path)  # remove volume from disk to save space

    return resampled_volume_sitk_obj, resampled_volume_nii_obj, resampled_volume_nii
