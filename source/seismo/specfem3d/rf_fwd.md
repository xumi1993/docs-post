# Reciver Function Forward simulation with Specfem3D_FWATR

:::{attention}
The Specfem3D_FWATR is under developing, so it has not been open accessed. Please be patient.
:::

## Preparation

For RF simulation, we invoked SEM-FK with plane wave injected to compute RFs, So parameter files are same as Specfem3D and SEM-FK, but an additional parameter file is required for RF parameters. 

### Common configures
- `DATA/Par_file`
- `DATA/meshfem3D_files`

### Exclusive configures
- `src_rec/sources_setXX.dat`: Map of source set `XX` and event id `YY`. The first field is read to define `YY`.
- `src_rec/FKmodel_YY.dat`
- `src_rec/STATION_YY.dat`