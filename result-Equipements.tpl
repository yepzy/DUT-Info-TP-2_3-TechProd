<table class="table table-striped">
%for values in equipements:
    <tr>
        %for value in values:
        	<td>{{value}}</td>
    </tr>
%end
</table>