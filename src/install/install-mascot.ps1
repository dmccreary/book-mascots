<#
.SYNOPSIS
  Install a single mascot's pose images into the local mkdocs project.

.DESCRIPTION
  Downloads 7 standard pose PNGs plus image-prompts.md from the
  published gallery at https://dmccreary.github.io/book-mascots/ into
  docs/img/mascot/ relative to the current working directory.

  Behavior is identical to the bash version (install-mascot.sh): the
  script takes a single positional argument (the mascot slug), creates
  docs/img/mascot/, downloads neutral / welcome / thinking / tip /
  encouraging / warning / celebration poses, saves them with bare
  filenames, and copies image-prompts.md as a reference.

.PARAMETER Slug
  The mascot slug (e.g. "intelligent-textbooks", "business",
  "us-government"). Find slugs at:
  https://dmccreary.github.io/book-mascots/install-mascot/

.EXAMPLE
  ./install-mascot.ps1 intelligent-textbooks

.LINK
  https://github.com/dmccreary/book-mascots
#>

param(
    [Parameter(Mandatory, Position = 0)]
    [string]$Slug
)

$ErrorActionPreference = 'Stop'

$BaseUrl = 'https://dmccreary.github.io/book-mascots/mascots'
$Target  = 'docs/img/mascot'
$Poses   = @('neutral', 'welcome', 'thinking', 'tip',
             'encouraging', 'warning', 'celebration')

# A handful of mascots use a name-prefix on each pose file (e.g.,
# axiom-neutral.png instead of neutral.png). Map those slugs to the
# prefix string used in their source filenames. Extend as needed.
function Get-PosePrefix([string]$s) {
    switch ($s) {
        'intelligent-textbooks' { return 'axiom-' }
        default                 { return '' }
    }
}

$Prefix = Get-PosePrefix $Slug

New-Item -ItemType Directory -Path $Target -Force | Out-Null
Write-Host "Installing mascot '$Slug' to $Target/"

$errors = 0
foreach ($pose in $Poses) {
    $url = "$BaseUrl/$Slug/$Prefix$pose.png"
    $out = Join-Path $Target "$pose.png"
    try {
        Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing `
            -ErrorAction Stop | Out-Null
        Write-Host "  ok  $pose.png"
    } catch {
        Write-Host "  ERR $pose.png  (tried $url)" -ForegroundColor Red
        $errors++
    }
}

# image-prompts.md is reference material; absence is non-fatal.
$promptsUrl = "$BaseUrl/$Slug/image-prompts.md"
$promptsOut = Join-Path $Target 'image-prompts.md'
try {
    Invoke-WebRequest -Uri $promptsUrl -OutFile $promptsOut `
        -UseBasicParsing -ErrorAction Stop | Out-Null
    Write-Host "  ok  image-prompts.md"
} catch {
    Write-Host "  --  image-prompts.md not available (non-fatal)"
    Remove-Item -Path $promptsOut -ErrorAction SilentlyContinue
}

if ($errors -gt 0) {
    Write-Host ''
    Write-Host "$errors pose(s) failed to download." -ForegroundColor Red
    Write-Host "Check that '$Slug' is a real mascot slug at:"
    Write-Host '  https://dmccreary.github.io/book-mascots/install-mascot/'
    Write-Host 'Or inspect the live gallery for this mascot at:'
    Write-Host "  $BaseUrl/$Slug/"
    exit 1
}

Write-Host ''
Write-Host "Installed '$Slug' to $Target/"
