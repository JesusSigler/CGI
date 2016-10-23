#!/usr/bin/perl
#
#PROGRAM: Create form CGI Program
#
#Purpose: Desmostrate (1) how to create a form complete in CGI doing
# 		so my first program CGI.	
#
#	Create by Jesus Sigler.
#

#-----------------------------------#
#  1. Create a new Perl CGI object  #
#-----------------------------------#

use CGI -utf8;
$query = new CGI;

#----------------------------------#
#  2. Print the doctype statement  #
#----------------------------------#

print $query->header;

#----------------------------------------------------#
#  3. Start the HTML doc, and give the page a title  #
#----------------------------------------------------#

print $query->start_html('My first form CGI');

#------------------------------------------------------------#
#  4.  If the program is called without any params, print   #
#       My dirst form CGI.                             #
#------------------------------------------------------------#

if (!$query->param) {
	print $query->start_form;
	print $query->h3('Personal data');
	print $query->label('Nombre: ');
	print $query->textfield(-name=>'nombre',
			-size=>25,
			-maxlength=>50);
	print $query->br;
	print $query->br;
	print $query->label('Apellidos: ');
	print $query->textfield(-name=>'apellidos',
			-size =>25,
			-maxlength=>50);
	print $query->br;
	print $query->br;
	print $query->label('Email: ');
	print $query->textfield(-name=>'email',
			-size =>25,
			-maxlength=>60);
	print $query->br;
	print $query->br;
	print $query->h3('Indica tu edad');
	print $query->radio_group(
        -name     => 'Checkbox',
        -values   => ['<10', '> 10 <= 18', '18', '>18'],
        -columns  => 2,
        -rows     => 2,
    );
    print $query->br;
    print $query->br;
    print $query->h4('Escribe aqui tu opinion sobre el formulario');
    print $query->textarea(
        -name  => 'textarea',
        -value => 'Write here...',
        -cols  => 60,
        -rows  => 3,
    );
open F, '/home/alumnado/Hobbies.txt' or die "No se puede abrir:$!";
while(<F>){
 chomp;
push (@Hobbies, $_);

}

close F;
	print $query->h3('Select your favorite hobby(ies): ');
	print $query->scrolling_list(-name=>'hobbies',
		-values=>\@Hobbies,
				 -size=>8,
				 -multiple=>'true');
	# Notes:
	# ------
	#	"-multiple=>'true'" lets the user make multiple selections
	#		from the scrolling_list
	#	"-default" is optional
	#	"-size" lets you specify the number of visible rows in the list
	#	can also use an optional "-labels" parameter to let the user
	#		see labels you want them to see, while you use
	#		different names for each parameter in your program
	
	print $query->br;
	print $query->br;
	print $query->submit(-value=>'Submit your Formulary');
	print $query->end_form;

} else {

	#----------------------------------------------------------#
	#  4b.  If the program is called with parameters, retrieve #
	#  the 'hobbies' parameter, assign it to an array        #
	#  named $hobbies, then print the array with each        #
	#  name separated by a <BR> tag.                           #
	#----------------------------------------------------------#

	print $query->h3('your favorites hobbies are:');
	@Hobbies = $query->param('hobbies');
	print "<BLOCKQUOTE>\n";
	foreach $hobbies (@Hobbies) {
		print "$hobbies<br>";
	}
	print "</BLOCKQUOTE>\n";

}

#--------------------------------------------------#
#  5. After either case above, end the HTML page.  #
#--------------------------------------------------#

print $query->end_html;

	


