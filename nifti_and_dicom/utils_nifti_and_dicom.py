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


def remove_zeros_ijk_from_volume(input_volume: np.ndarray) -> np.ndarray:
    """This function removes all the rows, columns and slices of the input volume that only contain zero values.
    Args:
        input_volume (np.ndarray): volume from which we want to remove zeros
    Returns:
        cropped_volume (np.ndarray): cropped volume (i.e. input volume with zeros removed)
    """
    def remove_zeros_one_coordinate(input_volume_: np.ndarray, range_spatial_dim: int, spatial_dim: int):
        idxs_nonzero_slices = []  # will the contain the indexes of all the slices that have nonzero values
        for idx in range(range_spatial_dim):  # loop over coordinate
            if spatial_dim == 0:
                one_slice = input_volume_[idx, :, :]
            elif spatial_dim == 1:
                one_slice = input_volume_[:, idx, :]
            elif spatial_dim == 2:
                one_slice = input_volume_[:, :, idx]
            else:
                raise ValueError("spatial_dim can only be 0, 1, or 2. Got {} instead".format(spatial_dim))

            if np.count_nonzero(one_slice) > 0:  # if the slice has some nonzero values
                idxs_nonzero_slices.append(idx)  # save slice index

        # retain only indexes with nonzero values from the two input volumes
        if spatial_dim == 0:
            cropped_volume_ = input_volume_[idxs_nonzero_slices, :, :]
        elif spatial_dim == 1:
            cropped_volume_ = input_volume_[:, idxs_nonzero_slices, :]
        elif spatial_dim == 2:
            cropped_volume_ = input_volume_[:, :, idxs_nonzero_slices]
        else:
            raise ValueError("spatial_dim can only be 0, 1, or 2. Got {} instead".format(spatial_dim))

        return cropped_volume_

    assert len(input_volume.shape) == 3, "The input volume must be 3D"

    # i coordinate
    cropped_volume = remove_zeros_one_coordinate(input_volume, input_volume.shape[0], spatial_dim=0)
    # j coordinate
    cropped_volume = remove_zeros_one_coordinate(cropped_volume, input_volume.shape[1], spatial_dim=1)
    # k coordinate
    cropped_volume = remove_zeros_one_coordinate(cropped_volume, input_volume.shape[2], spatial_dim=2)

    return cropped_volume


def get_axes_orientations_with_nibabel(input_nifti_volume: nib.Nifti1Image) -> tuple:
    """This function returns the axes orientations as a tuple
    Args:
        input_nifti_volume (nib.Nifti1Image): the input volume for which we want the axes orientations
    Returns:
        orientations (tuple): the axes orientations
    """
    aff_mat = input_nifti_volume.affine  # type: np.ndarray # extract affine matrix
    orientations = nib.aff2axcodes(aff_mat)
    
    return orientations


def get_nibabel_header(input_nifti_volume: nib.Nifti1Image,
                       print_header=False) -> nib.nifti1.Nifti1Header:
    """This function returns the header of the nifti image/volume
    Args:
        input_nifti_volume (nib.Nifti1Image): the input volume for which we want the header
        print_header (bool): whether to print the header or not; defaults to False
    Returns:
        header (nib.nifti1.Nifti1Header): the axes orientations
    """
    header = input_nifti_volume.header
    if print_header:
        print(header)
    
    return header
