$aux_dir = 'build';
$cleanup_includes_cusdep_generated = 1;
$cleanup_includes_generated = 1;
$pdf_mode = 1;
# biber ships as a universal binary and unpacks itself with "lipo -extract_family",
# a flag the current command line tools dropped; use a thinned copy when one exists
my $thin_biber = "$ENV{HOME}/bin/biber-arm64";
$biber = "$thin_biber %O %S" if -x $thin_biber;
