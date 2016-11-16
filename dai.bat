@echo off
IF [%1] EQU [clean] python ..\..\..\..\Build_Tools\CleanDir.py ..\DAG
IF [%1] NEQ [clean] python ..\..\..\..\Build_Tools\CopyCodeFiles.py ^
..\..\..\..\..\..\SWE3_EDS_SoftwareDetailedDesignAndUnitConstruction\SWE3_EDC_20_SW_Modules ..\DAG
IF [%1] NEQ [clean] python ..\..\..\..\Build_Tools\LookUpTable.py ..\DAG

build %1