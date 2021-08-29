####################################################
#  powershell script for packing the game 
#  the output is either a single exe file
#  or a folder containing the game files
####################################################

param(
    [Parameter(Mandatory=$true)][ValidateNotNullOrEmpty()][string]$type,
    [Parameter(Mandatory=$true)][ValidateNotNullOrEmpty()][string]$version
)

# function : Invoke-PrepareBuild
# purpose : prepares environment for build
# returns : 
function Invoke-PrepareBuild {
    if (Test-Path -Path "..\_build") {
        Write-Host "deleting existing directory ..."
        Remove-Item -Recurse -Force "..\_build" | Out-Null
    } 
    Write-Host "creating the _build directory ..."
    New-Item -ItemType Directory -Path "..\_build" | Out-Null
}

# function : New-Executable
# purpose : generates the executable using pyinstaller
# returns : true or false
function New-Executable {
    try {
        # dont forget the -wait argument to block execution while exe is generated
        Start-Process 'pyinstaller' `
                    -ArgumentList `
                        "--onefile", `
                        "--name lockdown", `
                        "..\..\lockdown\lockdown.py", `
                        "--paths ..\..\..\.venv\Lib\site-packages\", `
                        "--paths ..\..\lockdown", `
                        "--paths ..\..\lockdown\elements\", `
                        "--noconsole" `
                    -Wait
        return $true
    } catch {
        Write-Host "ERROR! error running pyinstaller"  -ForegroundColor White -BackgroundColor Red
        return $false
    }
}


# function : New-ZippedApplication
# purpose : generates the zipped application
# returns : 
function New-ZippedApplication {
    Write-Host "generating zipped application ..."
    New-Item -ItemType Directory -Path $build_folder | Out-Null
    # -recurse ensures that all files and folders under the folder is copied as well
    Copy-Item ..\..\assets -Destination $build_folder -Recurse
    Copy-Item .\dist\lockdown.exe -Destination $build_folder

    $zipped_filename = $build_folder + ".zip"
    # let us zip the application
    Compress-Archive -LiteralPath $build_folder -DestinationPath "..\..\_build\$($zipped_filename)"

    Write-Host "$($zipped_filename) was successfuly generated ..." -ForegroundColor White -BackgroundColor DarkGreen
}

# function : Invoke-Cleanup 
# purpose : cleanup no longer used files
# returns : 
function Invoke-Cleanup {
    Write-Host "cleaning up ...."
    Remove-Item -Force -Recurse ".\dist"
    Remove-Item -Force -Recurse ".\build"
    Remove-Item -Force -Recurse $build_folder
    Remove-Item "lockdown.spec"
    Set-Location -Path ..
    Remove-Item -Force -Recurse $build_folder
}

#######################################################################################
# the main function 
#######################################################################################

Write-Host "generation type : $($type)"
Write-Host "version : $($version)"

Invoke-PrepareBuild

# create the build folder with format lockdown_[version]

$build_folder = "lockdown_v" + $version

if (Test-Path -Path $build_folder) {
    Write-Host "deleting existing directory ..."
    Remove-Item -Recurse -Force $build_folder | Out-Null
}
Write-Host "creating the directory ..."
New-Item -ItemType Directory -Path $build_folder | Out-Null
Set-Location -Path $build_folder


if ($type -eq "file") {
    Write-Host "generating a single exe file at $($build_folder)...." -ForegroundColor Green
    if (New-Executable) {
        New-ZippedApplication
    } else {
        Write-Host "ERROR! no executable was generated" -ForegroundColor White -BackgroundColor Red
    }
} else {
    Write-Host "generating a package folder at $($build_folder)...." -ForegroundColor Green
    Write-Host "WARNING! this is not yet supported ..." -ForegroundColor White -BackgroundColor Red
    # for folder generated, no need to zip the folder
    # the output is meant to be used by an installer generating tool
}

Invoke-Cleanup
Write-Host "COMPLETE! game package generation is done. check for errors" -ForegroundColor White -BackgroundColor DarkGreen
Write-Host "##########################################################################"
Write-Host "###                                                                   ####"
Write-Host "###   the package is @ src\_build folder                              ####"
Write-Host "###                                                                   ####"
Write-Host "##########################################################################"
