from ..schemas import FileMetadataBase, FileMetadata

def parse_metadata(metadata_base: FileMetadataBase) -> FileMetadata:
    metadata = FileMetadata(
        name=metadata_base.name,
        size=metadata_base.size,
        csv_schema=metadata_base.csv_schema.split(','),
        checksum=metadata_base.checksum
    )

    return metadata